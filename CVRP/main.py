from CVRP.Algorithm.ALNS import solve

print("ALNS for Vehicle Routing Problem")
print("--------------------------------")
print("Ban hay nhap ten file trong thu muc CVRP\\Dataset de giai.\nLuu y: File ban can giai can \
co dinh dang khop voi cac file trong thu muc <ProjectPath>\\CVRP\\Dataset\\. Vi du: \"A-n36-k5\"")
file = input()
print("----------------------------------------------------")
solve(file)


