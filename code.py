final_position = input("enter final position")
path = input("enter path for intial position")

main_dir = {'f' :({'1e':'2n','1w':'5n','1u':'3n','1d':'6n','2n':'4w','2s':'1w','2u':'3w','2d':'6w',
             '3e':'2d','3w':'5d','3n':'4d','3s':'1d','4e':'2s','4w':'5s','4u':'3s','4d':'6s',
             '5n':'4e','5s':'1e','5u':'3e','5d':'6e','6e':'2u','6w':'5u','6n':'4u','6s':'1u'}),

            'b' :({'1e':'5n','1w':'2n','1u':'6n','1d':'3n','2n':'1w','2s':'4w','2u':'6w','2d':'3w',
             '3e':'5d','3w':'2d','3n':'1d','3s':'4d','4e':'5s','4w':'2s','4u':'6s','4d':'3s',
             '5n':'1e','5s':'4e','5u':'6e','5d':'3e','6e':'5u','6w':'2u','6n':'1u','6s':'4u'}),

            'l' :({'1e':'3n','1w':'6n','1u':'5n','1d':'2n','2n':'3w','2s':'6w','2u':'1w','2d':'4w',
             '3e':'4d','3w':'1d','3n':'5d','3s':'2d','4e':'6s','4w':'3s','4u':'2s','4d':'5s',
             '5n':'6e','5s':'3e','5u':'4e','5d':'1e','6e':'1u','6w':'4u','6n':'2u','6s':'5u'}),

            'r' :({'1e':'6n','1w':'3n','1u':'2n','1d':'5n','2n':'6w','2s':'3w','2u':'4w','2d':'1w',
             '3e':'1d','3w':'4d','3n':'2d','3s':'5d','4e':'3s','4w':'6s','4u':'5s','4d':'2s',
             '5n':'3e','5s':'6e','5u':'1e','5d':'4e','6e':'4u','6w':'1u','6n':'5u','6s':'2u'})

}

Direction = {'f':('f','f','f'),'b':'b','l':('l','l'),'r':('r','r')}

new_path =  []

for i in path:
    for key,value in Direction.items():
        if i == key:
            new_path.extend(value)

final = []
print("new path {}".format(new_path[::-1]))

for i in new_path[::-1]:
    for key, value in main_dir.items():
        if i == key:
            for k,v in value.items():
                if final_position in k:
                    final_position = v
                    print(final_position)
                    final.append(final_position)
                    break





