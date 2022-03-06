class SuperList(list):
    def __len__(self):
        return 1000


super_list = SuperList()
print(len(super_list))
