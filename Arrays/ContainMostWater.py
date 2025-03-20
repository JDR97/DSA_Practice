def waterAmount(height):
    n = len(height)
    max_area = 0
    left = 0
    right = n-1

    while(left < right):
        max_area = max(max_area, (right-left) * min(height[left], height[right]))
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

height = [1,8,6,2,5,4,8,3,7]
volume = waterAmount(height)
print(volume)