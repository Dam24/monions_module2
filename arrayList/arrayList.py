class ArrayList(object):

    def __init__(self, length=10):
        self.list = [0] * length
        self.elements = 0

    def append(self, value=None):
        if self.elements >= len(self.list):
            aux_list = [0] * (len(self.list) + 1)
            index = 0
            while index < len(self.list):
                aux_list[index] = self.list[index]
                index = index + 1
            self.list = aux_list

        self.list[self.elements] = value
        self.elements = self.elements + 1

    def search(self, index=None, value=None):
        if index:
            return self.list[index]
        index = 0
        while index < len(self.list):
            if self.list[index] == value:
                return self.list[index]
            index = index + 1

        raise ValueError("Data not in list")


    # def delete(self, index=None, value=None):


    #
	# def __str__(self):
	# 	s = ""
	# 	i=0
	# 	while i<self.elements:
	# 		s = s + str(self.list[i])
	# 		i=i+1
	# 		if i != self.elements:
	# 			s=s+","
	# 	return s
