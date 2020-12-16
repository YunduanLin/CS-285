# CS 285

## Policy Gradient
```
cd Documents/Codes/Course/CS285/project/code
```

## basic policy gradient
(Qianhua)
```
python cs285/scripts/run_parking.py -dsa --policy beta --exp_name b
python cs285/scripts/run_parking.py -dsa -rtg --policy beta -- exp_name b_rtg
python cs285/scripts/run_parking.py -rtg --policy beta -- exp_name b_rtg_sa
python cs285/scripts/run_parking.py -dsa --exp_name n
python cs285/scripts/run_parking.py -dsa -rtg -- exp_name n_rtg
python cs285/scripts/run_parking.py -rtg -- exp_name n_rtg_sa
```
(Yunduan)
```
python cs285/scripts/run_parking.py -dsa -rtg -l 2 --policy beta --exp_name b

```
## adjust network
```
```

## Actor-critic
```
python cs285/scripts/run_parking_actor_critic.py -ntu 100 -ngsptu 1
```