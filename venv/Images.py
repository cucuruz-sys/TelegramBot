from Parser import downloadImages
def main():
    item = "Гараж"
    downloadImages(item, 5, '../parser/' + item)
if __name__ == "__main__":
    main()
