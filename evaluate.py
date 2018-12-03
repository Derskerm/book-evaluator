import csv
import math
from searchtree import BookNode, BookData, RankData

book_tree = BookNode(BookData("","",-1))

def process_sheet():
    with open('books.csv', newline='') as csvfile:
        bookreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        last_pub = ""
        rec_list = {}
        init_flag = True
        for row in bookreader:
            entries = ' '.join(row).split(',')
            if entries[1]:
                if init_flag:
                    entries[0] = entries[0][1:]
                    last_pub = entries[0]
                    init_flag = False
                if entries[0] != last_pub:
                    add_recs(rec_list)
                    rec_list = {}
                    last_pub = entries[0]
                if entries[3] == '':
                    entries[3] = '1'
                datum = BookData(entries[1], entries[2], 0.0)
                rank = int(entries[3])
                if rank in rec_list:
                    rec_list[rank].append(datum)
                else:
                    rec_list[rank] = [datum]
        add_recs(rec_list)
            
ln2 = math.log(2)
def alg(value):
    return ln2 / math.log(value + 1)
    
def add_recs(rec_list):
    list_sum = sum([alg(x) for x in rec_list])
    list_size = sum([len(rec_list[x]) for x in rec_list])
    max_allotted = 1/alg(list_size)
    for rank in rec_list:
        rank_size = len(rec_list[rank])
        rank_multiplier = alg(rank)/list_sum
        for value in rec_list[rank]:
            value.rank = max_allotted * rank_multiplier / rank_size + 0.05
            book_tree.insert(value)

def print_ranking():
    book_list = book_tree.to_list()
    rank_tree = BookNode(RankData(book_tree.data))
    for book_datum in book_list:
        rank_tree.insert(RankData(book_datum))
    rank_tree.PrintTree()

def main():
    process_sheet()
    print_ranking()
  
if __name__== "__main__":
  main()