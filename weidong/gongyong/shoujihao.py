class Shoujihao():
    def shouji(self):
        shouji_txt = open(r'D:\job\object\shoujihao.txt')
        shouji = int(shouji_txt.read())
        print(shouji)
        t = shouji + 1
        shouji_txt.close()
        # shouji_txt = open("..\case\shoujihao.txt", 'w')
        shouji_txt = open("D:\job\object\shoujihao.txt", 'w')
        x = str(t)
        shouji_txt.write(x)
        shouji_txt.close()
        return shouji


if __name__ == "__main__":
    Shoujihao().shouji()


