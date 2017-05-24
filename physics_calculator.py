import sys
import math

def kinematics():
   d = input("\nDistance: ")
   vi = input("Initial Velocity: ")
   vf = input("Final Velocity: ")
   a = input("Acceleration: ")
   t = input("Time: ")
   print()
   
   try:
      d = float(d)
      d_lock = True
   except:
      d = False
      d_lock = False
   try:
      vi = float(vi)
      vi_lock = True
   except:
      vi = False
      vi_lock = False
   try:
      vf = float(vf)
      vf_lock = True
   except:
      vf = False
      vf_lock = False
   try:   
      a = float(a)
      a_lock = True
   except:
      a = False
      a_lock = False
   try:
      t = float(t)
      t_lock = True
   except:
      t = False
      t_lock = False

   i = 0
   
   while i<10 and not(type(d) == float and type(vi) == float and type(vf) == float and type(a) == float and type(t) == float):  
      if not d_lock and type(vi) == float and type(t) == float and type(a) == float:
         d = vi*t + 0.5*a*(t**2)
         d_lock = True
         print("Calculating")
      elif not a_lock and type(d) == float and type(vi) == float and type(t) == float:
         a = (d - vi*t)*2 / (t**2)
         a_lock = True
         print("Calculating")
      elif not vi_lock and type(d) == float and type(a) == float and type(t) == float:
         vi = (d - .5*a* t**2)/t
         vi_lock = True
         print("Calculating")

      if not vf_lock and type(vi) == float and type(a) == float and type(d) == float:
         vf = math.sqrt(vi**2 + 2*a*d)
         vf_lock = True
         print("Calculating")
      elif not vi_lock and type(vf) == float and type(a) == float and type(d) == float:
         vi = math.sqrt(vf**2 - 2*a*d)
         vi_lock = True
         print("Calculating")
      elif not d_lock and type(vf) == float and type(vi) == float and type(a) == float:
         d = (vf**2 - vi**2) / (2*a)
         d_lock = True
         print("Calculating")
      elif not a_lock and type(vf) == float and type(vi) == float and type(d) == float:
         a = (vf**2 - vi**2) / (2*d)
         a_lock = True
         print("Calculating")

      if not vf_lock and type(vi) == float and type(a) == float and type(t) == float:
         vf = vi + a*t
         vf_lock = True
         print("Calculating")
      elif not vi_lock and type(vf) == float and type(a) == float and type(t) == float:
         vi = vf - a*t
         vi_lock = True
         print("Calculating")
      elif not t_lock and type(vf) == float and type(vi) == float and type(a) == float:
         t = (vf - vi) / a
         t_lock = True
         print("Calculating")
      elif not a_lock and type(vf) == float and type(vi) == float and type(t) == float:
         a = (vf - vi) / t
         a_lock = True
         print("Calculating")

      if not d_lock and type(vi) == float and type(vf) == float and type(t) == float:
         d = (vi + vf) * t / 2
         d_lock = True
         print("Calculating")
      elif not t_lock and type(d) == float and type(vi) == float and type(vf) == float:
         t = 2 * d / (vi + vf)
         t_lock = True
         print("Calculating")
      elif not vf_lock and type(d) == float and type(vi) == float and type(t) == float:
         vf = (2*d/t) - vi
         vf_lock = True
         print("Calculating")
      elif not vi_lock and type(d) == float and type(vf) == float and type(t) == float:
         vi = (2*d/t) - vf
         vi_lock = True
         print("Calculating")

      i += 1

   if i == 10:
      print("Insufficient information.\n")
   else:
      print("\nDistance: {:.2f}".format(d))
      print("Initial Velocity: {:.2f}".format(vi))
      print("Final Velocity: {:.2f}".format(vf))
      print("Acceleration: {:.2f}".format(a))
      print("Time: {:.2f}\n".format(t))

if sys.argv[1] == '-k':
   kinematics()
