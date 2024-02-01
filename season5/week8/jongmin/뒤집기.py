S = input()

cnt = {
    "0" : S.split("0"),
    "1" : S.split("1")
}

"""for i in range(len(S)-1):
    if i!=len(S)-2:
        if S[i]!=S[i+1]:
            cnt[S[i]] += 1
    else:
        if S[i]!=S[i+1]:
            cnt[S[i]] += 1
            cnt[S[i+1]] += 1

print(min(cnt["0"],cnt["1"]))"""

arr1 = [i for i in cnt["0"] if i!=""]
arr2 = [i for i in cnt["1"] if i!=""]

print(min(len(arr1),len(arr2)))