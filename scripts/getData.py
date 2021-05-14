from fetch import fetchData
from process import processData


def getData():
    print(40*"=")
    print("WARNING: THIS COULD TAKE AROUND 15 MIN")
    print(40*"=")
    fetchData()
    processData()


if __name__ == '__main__':
    getData()
