def load_contents(filename):
    res = []
    with open(filename) as f:
        for line in f.readlines():
            for word in line.strip().split(' '):
                if word == '':
                    continue
                res.append(word)
    return res
    
    
def run():
    d = {}
    content = load_contents('main.txt')
    for word in content:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return most_used_10(d)

def most_used_10(d):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)[:10]

print(run())