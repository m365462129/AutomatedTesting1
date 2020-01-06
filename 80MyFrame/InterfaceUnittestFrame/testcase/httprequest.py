# -*- coding: UTF-8 -*-
import requests
import urllib


class HttpRequest:

	@classmethod
	def get_req(self, url):
		return requests.get(url)


	@classmethod
	def post_req(self, url, jsondata):
		return requests.post(url=url, data=jsondata)


	@classmethod
	def comb_url(self, url, jsonvalue):
		p = urllib.parse.urlencode(jsonvalue)
		if url.endswith("?"):
			res_url = url + p
		else:
			res_url = url + "?" + p
		return res_url


	@classmethod
	def req(self, protocol, url, data):
		if protocol == "get":
			res_url = self.comb_url(url, data)
			return self.get_req(res_url)
		elif protocol == "post":
			return self.post_req(url, data)