nums1 = [1,1,1,2,4,6,7]
nums2 = [1,2,3,6,7,8,9,10]
n1 = len(nums1)
n2 = len(nums2)
i = 0
j = 0
res = []
while i<n1 and j<n2:
    if nums1[i]<=nums2[j]:
        if len(res)==0 or nums1[i]!=res[-1]:
            res.append(nums1[i])
        i+=1
    else:
        if len(res)==0 or nums2[j]!=res[-1]:
            res.append(nums2[j])
        j+=1
while i<n1:
    if len(res)==0 or nums1[i]!=res[-1]:
        res.append(nums1[i])
    i+=1
while j<n2:
    if len(res)==0 or nums2[j]!=res[-1]:
        res.append(nums2[j])
    j+=1
print(res)