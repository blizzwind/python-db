import os

def run():
  try:
    os.mkdir("__db__")
  except:
    return "error"
  return "system opened"

def exc(q):
  q = q.split(" ")
  if q[0] == "c":
    if q[1] == "db" and len(q) == 3:
      try:
        os.mkdir("__db__/"+q[2])
        return "database created"
      except:
        return "error"
    elif q[1] == "db" and q[3] == "table" and len(q) == 5:
      try:
        f = open("__db__/"+q[2]+"/"+q[4]+".pydb", "x")
        f.close()
        return "table created"
      except:
        return "error"
    elif q[1] == "db" and q[3] == "table" and len(q) >= 6:
      try:
        s = q[5]
        for i in range(6, len(q)):
          s += " "+q[i]
        f = open("__db__/"+q[2]+"/"+q[4]+".pydb", "a")
        s = s+"\n"
        f.write(s)
        f.close()
        return "data created"
      except:
        return "error"
    else:
      return "error"
  elif q[0] == "r":
    if q[1] == "db" and q[3] == "table" and len(q) >= 6:
      try:
        d = []
        s = q[5]
        for i in range(6, len(q)):
          s += " "+q[i]
        s = s.split("=")
        if s[0].endswith(" "):
          s[0] = s[0][:-1]
        if s[1].startswith(" "):
          s[1] = s[1][1:]
        t_1 = s[0]+":"+s[1]
        t_2 = s[0]+" :"+s[1]
        t_3 = s[0]+": "+s[1]
        t_4 = s[0]+" : "+s[1]
        f = open("__db__/"+q[2]+"/"+q[4]+".pydb", "r")
        for l in f.readlines():
          if t_1 in l or t_2 in l or t_3 in l or t_4 in l:
            d.append(l[:-1])
        f.close()
        return d
      except:
        return "error"
    else:
      return "error"
  elif q[0] == "u":
    if q[1] == "db" and q[3] == "table" and len(q) >= 6:
      try:
        d = ""
        s = q[5]
        for i in range(6, len(q)):
          s += " "+q[i]
        s = s.split("=")
        if s[0].endswith(" "):
          s[0] = s[0][:-1]
        if s[1].startswith(" "):
          s[1] = s[1][1:]
        if s[1].endswith(" "):
          s[1] = s[1][:-1]
        if s[2].startswith(" "):
          s[2] = s[2][1:]
        old_t_1 = s[0]+":"+s[1]
        old_t_2 = s[0]+" :"+s[1]
        old_t_3 = s[0]+": "+s[1]
        old_t_4 = s[0]+" : "+s[1]
        new_t = s[0]+":"+s[2]
        f = open("__db__/"+q[2]+"/"+q[4]+".pydb", "r")
        for l in f.readlines():
          l = l.replace(old_t_1, new_t)
          l = l.replace(old_t_2, new_t)
          l = l.replace(old_t_3, new_t)
          l = l.replace(old_t_4, new_t)
          d += l
        f.close()
        f = open("__db__/"+q[2]+"/"+q[4]+".pydb", "w")
        f.write(d)
        f.close()
        return "successfully updated"
      except:
        return "error"
    else:
      return "error"
  elif q[0] == "d":
    if q[1] == "db" and q[3] == "table" and len(q) >= 6:
      d = ""
      s = q[5]
      for i in range(6, len(q)):
        s += " "+q[i]
      s = s.split("=")
      if s[0].endswith(" "):
        s[0] = s[0][:-1]
      if s[1].startswith(" "):
        s[1] = s[1][1:]
      t_1 = s[0]+":"+s[1]
      t_2 = s[0]+" :"+s[1]
      t_3 = s[0]+": "+s[1]
      t_4 = s[0]+" : "+s[1]
      f = open("__db__/"+q[2]+"/"+q[4]+".pydb", "r")
      for l in f.readlines():
        if t_1 in l or t_2 in l or t_3 in l or t_4 in l:
          pass
        else:
          d += l
      f.close()
      f = open("__db__/"+q[2]+"/"+q[4]+".pydb", "w")
      f.write(d)
      f.close()
      return "successfully deleted"
    else:
      return "error"
  else:
    return "error"
