#!/usr/bin/python

import os
import sys

def crawling(iurl):
	urlObj = urllib.openurl(iurl)
	data = urlObj.text
	return data

if __name__ == "__main__":
	crawling()
