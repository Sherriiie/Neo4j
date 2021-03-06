# -*- coding: utf-8 -*-
# !/usr/bin/env python

# from __future__ import print_function

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import readData
from py2neo import Node, Relationship, Graph, authenticate

'''
Creat a graph database with regards to artists and their works.
you should start your neo4j server first in the shell with commond.
'''

# set up authentication parameters
authenticate("localhost:7474", "neo4j", "sherrie")
# connect to authenticated graph database
# graph = Graph("http://localhost:7474/db/data/")
graph = Graph()
graph.delete_all()
cypher = graph.cypher


def create_artist_node(file_path, num_author):
	artists = readData.read_artists(file_path)
	nodes = list()
	for artist in artists:
		num_author += 1
		node = Node(u"Person", idx=num_author,
		            name=artist.name,
		            job=artist.job,
		            birthPlace=artist.birthPlace,
		            nationality=artist.nationality,
		            works=artist.works,
		            artisticStyple=artist.artisticStyple,
		            worksType=artist.worksType,
		            birthDate=artist.birthDate,
		            causeOfDeath=artist.causeOfDeath,
		            achievement=artist.achievement)
		nodes.append(node)
	return nodes, num_author


def create_work_node(file_path, num_work):
	works = readData.read_works(file_path)
	nodes = list()
	for work in works:
		num_work += 1
		node = Node(u"Work", idx=num_work,
		            name=work.name,
		            type=work.type,
		            createdBy=work.createdBy,
		            createdTime=work.createdTime,
		            size=work.size,
		            tone=work.tone,
		            style=work.style,
		            owner=work.owner,
		            value=work.value)
		nodes.append(node)
	return nodes, num_work


num_author = 0
num_work = 0
artist_nodes, num_author = create_artist_node('./data/artist.xlsx', num_author)
work_nodes, num_work = create_work_node('./data/work.xlsx', num_work)
print len(work_nodes)

for work in work_nodes:
	artist_name = work["createdBy"]
	print artist_name
	for artist in artist_nodes:
		if artist["name"] == artist_name:
			relationship = Relationship(artist, u"创作", work)
			graph.create(relationship)
