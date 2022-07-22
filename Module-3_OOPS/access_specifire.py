class student:
    __stid=12
    __stnm="Hemang"

    def getdata(self):
        print("Student ID:",self.__stid)
        print("Student Name:",self.__stnm)

    def __getsum(self,a,b):
        print("SUm:",a+b)
    
    def answer(self):
        self.__getsum(23,54)

st=student()
st.getdata()
st.answer()