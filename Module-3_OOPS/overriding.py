class student:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)


class otherstudent(student):
    def getdata(self, id, name):
        return super().getdata(id, name)


st=student()
st.getdata(34,'Hitesh')

ot=otherstudent()
ot.getdata(12,'Nirav')