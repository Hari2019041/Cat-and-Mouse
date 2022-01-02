from config import *

def distance(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

def point_on_circle(angle, radius=RADIUS):
    return CENTER[0]+radius*cos(angle), CENTER[1]-radius*sin(angle)

def calculate_angle(C, O=CENTER, A=point_on_circle(0)):
    OC = distance(O, C); AC = distance(A, C); OA = distance(O, A)
    if OC != 0:
        angle = acos((OC**2+OA**2-AC**2)/(2*OA*OC))
        angle = 2*pi-angle if A==point_on_circle(0) and C[1]>O[1] else angle
    else:
        angle = 0
    return angle

def create_tangent(point):
    angle = calculate_angle(point)
    tangent_angle = (angle-pi/2)%(2*pi)
    tangent_point = point_on_circle(angle)
    r = 100
    tangent = tangent_point[0]+r*cos(tangent_angle), tangent_point[1]-r*sin(tangent_angle)
    return tangent_point, tangent
