#we want to put the ray into a line
#and then compare that line to the segment
from math import tan,pi,atan2

def line_from_segment(seg):
    x1=seg[0][0]
    y1=seg[0][1]
    x2=seg[1][0]
    y2=seg[1][1]
    if x2==x1:
        return [1,0,-x1]
    else:
        m=(y2-y1)/(x2-x1)
        b=y1-m*x1
        lst=[m,-1,b]
        return lst

def line_from_ray(ray):
    point=ray[0]
    angle=ray[1]
    x=point[0]
    y=point[1]
    if angle == pi/2 or angle == -pi/2:
        return [1,0,-x]
    else:
        m=tan(angle)
        c = y-m*x
        return [m,-1,c]

def lines_intersect(line1,line2):
    line1_x=line1[0]
    line1_y=line1[1]
    line1_c=line1[2]
    line2_x=line2[0]
    line2_y=line2[1]
    line2_c=line2[2]
    denom=line1_x*line2_y-line1_y*line2_x
    lst=[]
    if denom==0:
        return "None"
    else:
        num_x=line1_y*line2_c-line1_c*line2_y
        num_y=line1_c*line2_x-line1_x*line2_c
        x=num_x/denom
        y=num_y/denom
        lst.append(x)
        lst.append(y)
        return lst

def point_on_segment(point,seg):
    a=point[0]
    b=point[1]
    c=seg[0][0]
    d=seg[0][1]
    e=seg[1][0]
    f=seg[1][1]
    if a > max(c,e) or a < min(c,e):
        return False
    if b > max(d,f) or b < min(d,f):
        return False
    else:
        return True

def point_on_ray(point,ray):
    x=point[0]
    y=point[1]
    start_x=ray[0][0]
    start_y=ray[0][1]
    angle = ray[1]
    while angle > pi:
        angle = angle - 2*pi
    while angle < -pi:
        angle = angle + 2*pi
    ray=[ray[0],angle]
    rounding=10e-15
    if angle == pi or angle==-pi or angle== pi/2 or angle==-pi/2 or angle==0:
        if angle == pi or angle == -pi:
            if x<start_x and abs(y-start_y)<rounding:
                return True
            else:
                return False
        if angle == pi/2:
            if abs(x-start_x)<rounding and y>start_y:
                return True
            else:
                return False
        if angle == -pi/2:
            if abs(x-start_x)<rounding and y<start_y:
                return True
            else:
                return False
        if angle ==0:
            if x>start_x and abs(y-start_y)<rounding:
                return True
            else:
                return False
    else:
        if angle>0 and angle<pi/2:
            if x>start_x and y>start_y:
                return True
            else:
                return False
        if angle >pi/2 and angle < pi:
            if x<start_x and y>start_y:
                return True
            else:
                return False
        if angle <0 and angle>-pi/2:
            if x>start_x and y<start_y:
                return True
            else:
                return False
        if angle <-pi/2 and angle >-pi:
            if x<start_x and y<start_y:
                return True
            else:
                return False
    
def ray_segment_intersect(ray,seg):
    line1 = line_from_ray(ray)
    line2 = line_from_segment(seg)
    m=lines_intersect(line1,line2)
    if m=="None":
        return "None"
    else:
        if point_on_segment(m,seg) and point_on_ray(m,ray):
            return m
        else:
            return "None"

def line_segments_from_window(window):
    x1=window[0][0]
    x2=window[0][1]
    y1=window[1][0]
    y2=window[1][1]
    start_x = min(x1,x2)
    end_x = max(x1,x2)
    start_y = min(y1,y2)
    end_y = max(y1,y2)
    first = [[start_x,start_y],[start_x,end_y]]
    second = [[start_x,end_y],[end_x,end_y]]
    third = [[end_x,end_y],[end_x,start_y]]
    fourth = [[end_x,start_y],[start_x,start_y]]
    return [first,second,third,fourth]

def ray_window_intersect(ray,win):
    i=0
    m=0
    seg_from_win = line_segments_from_window(win)
    while i<len(seg_from_win):
        inter = ray_segment_intersect(ray,seg_from_win[i])
        if inter != "None":
            m=inter
        i=i+1
    return m
    
def one_bounce(ray,seg,win):
    point=ray[0]
    angle = ray[1]
    x3 = seg[0][0]
    y3 = seg[0][1]
    x4 = seg[1][0]
    y4 = seg[1][1]
    while angle > pi:
        angle = angle -2*pi
    while angle < -pi:
        angle = angle + 2*pi
    ray=[point,angle]
    rise = [2.55, 0.44999999999999996]
    if rise == "None":
        leave_win = ray_window_intersect(ray,win)
    else:
        x2=rise[0]
        y2=rise[1]
        x1=point[0]
        y1=point[1]
        v_in = [x2-x1,y2-y1]
        mag_v_in = (v_in[0]**2+v_in[1]**2)**0.5
        unit_v_in = [v_in[0]/mag_v_in,v_in[1]/mag_v_in]
        #s means segment 
        s = [x3-x4,y3-y4]
        mag_s = (s[0]**2+s[1]**2)**0.5
        unit_s = [s[0]/mag_s,s[1]/mag_s]
        # . means dot product 
        #call s_n = normal to segment, lets say s=[s1,s2]
        #s.s_n = 0, therefore:
        #s1*(x3-x4)+ s2*(y3-y4)=0
        #s2 = -s1*(x3-x4)/(y3-y4)
        #we can sub in x2 for s1 as (x2,y2) lies on s_n, so:
        s2 = -x2*(x3-x4)/(y3-y4)
        s_n = [x2,s2]
        mag_s_n = (s_n[0]**2+s_n[1]**2)**0.5
        unit_s_n = [x2/mag_s_n,s2/mag_s_n]
        # v_out = -unit_v_in + 2*a
        # a = (projection of -v_in onto s_n) + unit_v_in
        # projection of -v_in onto s_n = -unit_v_in . s_n
        # mag(s_n) does not matter as it is 1
        scalar = -1*unit_v_in[0]*unit_s_n[0] + (-1*unit_v_in[1]*unit_s_n[1])
        # the actual projection is the scalar times s_n
        proj = [s_n[0]*scalar, s_n[1]*scalar]
        a = [proj[0]+unit_v_in[0],proj[1]+unit_v_in[1]]
        v_out = [-v_in[0] + 2*a[0], -v_in[1] + 2*a[1]]
        mag_v_out = (v_out[0]**2+v_out[1])**0.5
        unit_v_out = [v_out[0]*mag_v_out,v_out[1]*mag_v_out]
        x=unit_v_out[0]
        y=unit_v_out[1]
        new_angle = atan2(y,x)
        new_ray = [rise,new_angle]
        leave_win = ray_window_intersect(new_ray,win) 
    return [point,rise,leave_win]


seg=[[0,3],[3,0]]
win=[[-1,4],[-1,4]]
ray=[[1,1],pi/4]
print(one_bounce(ray,seg,win))
    
