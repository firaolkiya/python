class Solution(object):
    def convertTemperature(self, celsius):
        kelven = float(celsius + 273.15)
        far = (celsius * 1.80 )+32.00

        k = []
        k.append(kelven)
        k.append(far)

        return k
        