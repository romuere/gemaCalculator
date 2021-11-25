# ## Atividade 3 (Letra c) - Modelos Mistos

import numpy as np
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

#import sys

class Henderson():
    
    def __init__(self, bancodedados,salvar):
        
        self.matriz = np.loadtxt(bancodedados,delimiter=',',dtype=np.int32,skiprows=1)
        matriz2 = np.zeros((self.matriz.shape[0]+1,self.matriz.shape[1]+1))
        matriz2[1:,1:] = self.matriz
        self.matriz = np.asarray(matriz2,dtype=np.int32)
        self.salvar = salvar
        
    def calculo(self):
        
        f = open(self.salvar,'w')
        print(" Banco de Dados:\n",self.matriz[1:,1:], file=f)
        #print(" Banco de Dados:\n",self.matriz[1:,1:])

        # ##### Rounds
        n_individuos = self.matriz.shape[0]-1
        v = np.zeros((n_individuos+1))
        u = np.zeros((n_individuos+1))
        d_ = np.zeros((n_individuos+1))
        d_i = np.zeros((n_individuos+1))
        l = []
        #i=1
        for i in range(1,n_individuos+1):
            print('------------------------------------------------------------------------',file=f)
            s = self.matriz[i,2]
            d = self.matriz[i,3]
            #print(s,d)
            if (s==0) & (d==0):
                v[i] = 1
            elif (s>0) & (d>0):
                #print('aqui')
                v[i] = (1-((1/4)*(u[s]+u[d])))**(1/2)
            elif (s>0) & (d==0):
                v[i] = (1-(1/4)*(u[s]))**(1/2)
            elif (s==0) & (d>0):
                v[i] = (1-(1/4)*(u[d]))**(1/2)

            ##u
            j=i
            u[j] = u[j]+v[j]**2

            j = i+1
            while j<=n_individuos:
            #while j<=4:
                s = self.matriz[j,2]
                d = self.matriz[j,3]
                #print('i=',i,'s=',s,'d=',d,'j=',j)
                if (s<i) & (d<i):
                    v[j] = 0
                    #print('aqui')
                elif (i<=s) & (i<=d):

                    v[j] = ((1/2)*(v[s]))+((1/2)*(v[d]))
                    #print('aqui1')
                elif (d<i) & (i<=s):
                    #print(v[s])
                    v[j] = (1/2)*(v[s])
                    #print('aqui2')
                elif (s<i) & (i<=d):
                    v[j] = (1/2)*(v[d])
                    #print('aqui3')

                u[j] = u[j]+(v[j]**2)
                #print('u{} = {}'.format(j,u[j]))
                j += 1
            l.append(np.copy(v[1:]))
            d_[i] = v[i]**2
            d_i[i] = v[i]**(-2)
            
            print('Rodada ',i,file=f)
            print('v = ',v[1:],file=f)
            print('\nu = ',u[1:],file=f)
            print('\nd = ',d_[1:],file=f)
            print('\nd_i = ',d_i[1:],file=f)


        # ## Montando matriz


        l = np.asarray(l)
        l = np.tril(np.transpose(l))
        print("Matriz L:\n", l,file=f)


        A = np.matmul(l,np.transpose(l))
        print("Matriz A:\n",A,file=f)


        # ## Inversa de A

        print("Obtenção de A-1",file=f)
        A_i = np.zeros((n_individuos+1,n_individuos+1))
        for i in range(1,n_individuos+1):
            A_inv = np.zeros((n_individuos+1,n_individuos+1))
            s = self.matriz[i,2]
            d = self.matriz[i,3]
            if (s>0) & (d>0):
                A_inv[i,i] = d_i[i]
                A_inv[i,s] = A_inv[i,d] = A_inv[s,i] = A_inv[d,i] = (-1/2)*d_i[i]
                A_inv[s,s] = A_inv[s,d] = A_inv[d,s] = A_inv[d,d] = (1/4)*d_i[i]
            elif (s>0) & (d==0):
                A_inv[i,i] = d_i[i]
                A_inv[i,s] = A_inv[s,i] = (-1/2)*d_i[i]
                A_inv[s,s] = (1/4)*d_i[i]
            elif (s==0) & (d>0):
                A_inv[i,i] = d_i[i]
                A_inv[i,d] = A_inv[d,i] = (-1/2)*d_i[i]
                A_inv[d,d] = (1/4)*d_i[i]
            elif (s==0) & (d==0):
                A_inv[i,i] = d_i[i]
            print('--------------------------Individuo {}--------------------------'.format(i),file=f)
            A_i += A_inv
            print(A_i[1:,1:],file=f)
