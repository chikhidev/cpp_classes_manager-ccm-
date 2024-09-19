# cpp_classes_manager-ccm-
a util you can use to easly manage your (create, deletion, ...) of your classes in cpp
i will be adding more features in the future by time (in-chaellah)

## Setup
```
    git clone https://github.com/chikhidev/cpp_classes_manager-ccm-.git ~/ccm
    cd ccm
    echo "alias ccm='python3 ~/ccm/ccm.py'" >> ~/.bashrc
    source ~/.bashrc
```
now you are good to go 🥳

## Available commands for now:
```
    ccm create <name-of-class> <name-of-class1> <name-of-class2>
    ccm remove <name-of-class> <name-of-class1> <name-of-class2>
    ccm addto <name-of-class> <method-return-type> <method-name> <function-arg1> <function-arg2> <function-arg3>
```
Examples:
```
    ccm create user player "football player" food
    ccm remove User Food
    ccm addto  User             void  createUser  std::string:name  int:id  bool:verified
    ccm addto  FootballPlayer   int   totalScore  int:match_id
```

By default the name of the classes forced to become in CAMEL-CASE

use ```ccm help``` to display all the available operations in time!

Thank you.