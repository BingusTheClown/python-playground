class SearchAlgorithms:

	def linearSearchString(desiredString, stringArray):
		if not (isinstance(stringArray, list) and all(isinstance(elem, str) for elem in stringArray)):
			raise ValueError('Expected an array of strings')
		if not isinstance(desiredString, str):
			raise ValueError('Expected a string')
		for i in stringArray:
			if (i == desiredString):
				return True
		return False