R=range;L=len;E=lambda b:[*map(list,zip(*b))];D=['l','u','uf','ls','lf']#Refact in the near future
def T(b,d,tmp=0):
    if tmp:return T([r[::-1]for r in b],d)
    else:g=[[],[]];c=[[],[]];m=[];size=[L(b),L(b[0])];g[1],c[1]=idx(b,d);g[0],c[0]=idx(b,0)
    if b[0][0]==d:return[]
    if not g[1]:return T(E(b),d)
    if not c[1]-c[0]:c[0]!=size[1]-1 and(m:=m+[b[g[0]][c[0]+1]])or(m:=m+[b[g[0]][c[0]-1]])
    elif not c[0]:m+=[b[r][0]for r in R(g[0]-1,g[1]-1,-1)]+b[g[1]][1:c[1]+1]
    else:j=slide(b,(m:=m+[b[g[0]-1-r][c[0]]for r in R(g[0])]+b[0][c[0]-1::-1]));m+=[j[r+1][0]for r in R(g[1])]+j[g[1]][1:c[1]+1]
    return m+T((h:=slide(b,m)),d)
def F(b,n):
    r,c=idx(b,n);ch=(n-1)//L(b[0])-L(b[0])+2
    if(z:=(n-1)%L(b[0]))==c and ch==r:return[]
    if z<=c and not ch:return T([r[z:]for r in b],n)
    elif z<=c and ch:return(m:=U(b,[0,max(c,z+2)],'lf'))+F((h:=slide(b,m)),n)
    elif z>c:h=slide((h:=slide(b,(m:=U(b,[0,max(c+1,2)],'lf')))),(q:=U(h,[0,max(c+1,2)],'lf')));return m+q+F(h,n)
def idx(b,d):
    for i in R(L(b)):
        if d in b[i]:return[i,b[i].index(d)]
def Z(b):r,c=idx(b,0);return[b[i][c]for i in R(r+1,L(b))]+[b[L(b)-1][i]for i in R(c+1,L(b[0]))]
def slide(b,m):
    if m==[]:return b
    h=[r[:]for r in b];q=m[0];rest=m[1:];r=[[],[]];c=[[],[]];r[1],c[1]=idx(b,q);r[0],c[0]=idx(b,0)
    if r[1]>0 and h[r[1]-1][c[1]]==0:h[r[1]-1][c[1]]=h[r[1]][c[1]];h[r[1]][c[1]]=0;r[0]+=1
    elif r[1]<L(h)-1 and h[r[1]+1][c[1]]==0:h[r[1]+1][c[1]]=h[r[1]][c[1]];h[r[1]][c[1]]=0;r[0]-=1
    elif c[1]>0 and h[r[1]][c[1]-1]==0:h[r[1]][c[1]-1]=h[r[1]][c[1]];h[r[1]][c[1]]=0;c[0]+=1
    else:h[r[1]][c[1]+1]=h[r[1]][c[1]];h[r[1]][c[1]]=0;c[0]-=1
    return(h:=slide(h,rest))if rest!=[]else h
def P(b):return[b[1][1],b[1][0],b[0][0],b[0][1],b[0][2],b[1][1],b[1][0],b[0][0],b[0][1],b[0][2],b[0][0],b[1][0],b[1][1],b[0][0],b[0][2],b[0][1],b[1][0],b[1][1]]
def slide_puzzle(b):
    def V(b,n):
        r,c=idx(b,n);rp=(n-1)//len(b[0]);cp=(n-1)%len(b[0]);h=[r[:]for r in b];m=[]
        if (r!=rp) and (h:=slide(h,(m:=m+T(h[min(r,L(b)-2):],n,tmp=1)))):
            if cp==L(b[0])-1:
                m+=Z(h);r,c=idx((h:=slide(h,Z(h))),n)
                for i in R(r,rp,-1):h=slide(h,(q:=U(h,[max(i,rp+2),cp-1],'uf')));m+=q
                return m
        m+=T([r[cp:]for r in h[rp:]],n);return m
    n,res=len(b),[]
    for i in R(1,n*(n-2)+1):b,res=slide(b,(m:=Z(b))),res+m;b,res=slide(b,(m:=V(b,i))),res+m
    for i in R(n*(n-2)+1,n**2-2):b,res=slide(b,(m:=Z(b))),res+m;b,res=slide(b,(m:=F(b[-2:],i))),res+m
    return None if b[-1][-2]!=n**2-1 else res
def U(b,c,dc):
    s,q=[L(b),L(b[0])],[];path=[b[s[0]-1][-r]for r in R(1,L(b[0])-c[1])]+[b[-r][c[1]]for r in R(1,len(b)-c[0]+1)];path.pop(0);m=path[:];h=slide(b,m)
    if dc==D[0]:q+=P([r[c[1]-2:c[1]+1]for r in h[c[0]-1:c[0]+1]])
    elif dc=='u':q+=P(E([r[c[1]-1:c[1]+1]for r in h[c[0]-2:c[0]+1]]))
    elif dc=='uf':c[1]!=0 and(q:=q+P(E([r[c[1]+1:c[1]-1:-1]for r in h[c[0]-2:c[0]+1]])))or(q:=q+P(E([r[c[1]+1::-1]for r in h[c[0]-2:c[0]+1]])))
    elif dc=='lf':return U(E(b),c[::-1],'uf')
    h=slide(h,q);m+=q;c!=[s[0]-1,s[1]-2]and(m:=m+path[::-1])or(m:=m+[h[s[0]-1][s[1]-1]]);return m