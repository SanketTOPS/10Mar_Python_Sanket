class student:
    stid=101
    stnm="Sanket"

    def printdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)

# Object
"""st=student()
st.printdata()
st.stid=102
st.stnm="Mitesh"
st.printdata()
"""

# Instance
student().printdata()

student().stid=102
student().stnm="Hitesh"

student().printdata()
