class Solution:
    def removeElement(self, numbers: List[int], value: int) -> int:
        ir = 0
        iw = 0
        k = 0
        for i in numbers:
            if numbers[ir] != value:
                numbers[iw] = numbers[ir]
                iw += 1
            ir += 1
        return iw
