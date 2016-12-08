# -*- coding: utf-8 -*-
#!/usr/bin/env python

# from __future__ import print_function
import readData
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from py2neo import Graph, authenticate
from neo4j.v1 import GraphDatabase, basic_auth

'''
make your queries here 
'''
# set up authentication parameters
authenticate("localhost:7474", "neo4j", "sherrie")
# connect to authenticated graph database


# graph = Graph("http://localhost:7474/db/data/")
graph = Graph()
cypher = graph.cypher

statement = "MATCH (a:Person) RETURN a.name AS name, a.job AS job"
driver = GraphDatabase.driver("bolt://localhost", auth = basic_auth("neo4j", "sherrie"))
sess = driver.session()
records = sess.run(statement = statement)
for record in records:
	print record["name"], record["job"]
	print record
print "finished"
sess.close()



def get_inf_paintingName(id_painting = 1):
	name = cypher.execute("match (work:Work {idx:«r2»}) return work.name", r2=id_painting)
	work = cypher.execute("match (work:Work {idx:«r2»}) return work", r2=id_painting)
	# print work

	return name, work
def get_inf_painter(id_painting = 1):
	painter_name= cypher.execute("match (painter:Person) -[:«p1»]-> (work:Work {idx:«p2»})  return painter.name", p1 = u"创作", p2=id_painting)
	painter = cypher.execute("match (painter:Person) -[:«p1»]-> (work:Work {idx:{p2}})  return painter",
	                              p1=u"创作", p2=id_painting)
	return painter_name ,painter

if __name__ == "__main__":
	# name = get_inf_paintingName(1)
	# name,work = get_inf_paintingName(1)
	# length = len(work.records)
	# print name
	# print 'length = {}'.format(length)
	# print work[0]
	# print work
	painter_name, painter = get_inf_painter(1)
	print painter_name
	print (painter[0])



