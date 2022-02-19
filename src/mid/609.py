from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = {}
        for path in paths:
            files = path.split(' ')
            dir = files[0].strip()
            for file in files[1:]:
                x = file.split('(')
                f = x[0].strip()
                content = x[1].replace(")", "").strip()
                if content not in d:
                    d[content] = []
                d[content].append(dir + "/" + f)
        ans = []
        for k, v in d.items():
            if len(v) > 1:
                ans.append(v)
        return ans


s = Solution()
print(s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))
print(s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]))