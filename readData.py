# coding: utf-8

import xlrd, xlwt
import numpy as np
import random
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

'''
read (author and work) data from xlsx to create object
'''


def read_data(file_name):
	'''
	:param file_name: the file to read
    read all the properties of the author in .xlsx
    :return
    '''
	data = xlrd.open_workbook(file_name)
	tables = data.sheets()
	props_list = list()
	for table in tables:
	# table = data.sheet_by_name(sheet_name=name)  # unicode encoding
		nrows = table.nrows
		# print ("the total row in table is " + str(nrows))
		props = dict()
		for i in range(1, nrows):
			row= table.row(i)
			props[row[0].value] = row[1].value
		props_list.append(props)
	return props_list

def read_artists(file_path):
	props_list = read_data(file_path)
	artists = list()
	for props in props_list:
		artist = Artist(props)
		artists.append(artist)
	return artists


def read_works(file_path):
	props_list = read_data(file_path)
	works = list()
	for props in props_list:
		work = Work(props)
		works.append(work)
	return works

class Artist(object):
	def __init__(self, props):
		# print props
		self.name = props['name']
		self.job = props['job']
		self.birthPlace = props['birthPlace']
		self.nationality = props['nationality']
		self.works = props['works']
		self.artisticStyple = props['artisticStyle']
		self.worksType = props['worksType']
		self.birthDate = props['birthDate']
		self.causeOfDeath = props['causeOfDeath']
		self.achievement = props['achievement']


class Work(object):
	def __init__(self, props):
		# print props
		self.name = props['name']
		self.type = props['type']
		self.createdBy = props['createdBy']
		self.createdTime = props['createdTime']
		self.size = props['size']
		self.tone = props['tone']
		self.style = props['style']
		self.owner = props['owner']
		self.value = props['value']



if __name__ == "__main__":
	print ''