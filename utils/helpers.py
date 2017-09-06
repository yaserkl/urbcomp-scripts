#Helper function to plot networks.

from __future__ import absolute_import
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import seaborn as sns

def plot_network(g,node_dist=1.0,nodecolor='g',nodesize=1200,nodealpha=0.6,edgecolor='k',\
                 edgealpha=0.2,figsize=(9,6),title=None,titlefontsize=20,savefig=False,\
                 filename=None,bipartite=False,bipartite_colors=None):
    pos=nx.spring_layout(g,k=node_dist)
    nodes=g.nodes()
    edges=g.edges()
    plt.figure(figsize=figsize)
    
    nx.draw_networkx_edges(g,pos=pos,edge_color=edgecolor,alpha=edgealpha)
    if bipartite and bipartite_colors!=None:
        bipartite_sets=nx.bipartite.sets(g)
        _nodecolor=[]
        for _set in bipartite_sets:
            _clr=bipartite_colors.pop()
            for node in _set:
                _nodecolor.append(_clr)
        
        nx.draw_networkx_nodes(g,pos=pos,node_color=_nodecolor,alpha=nodealpha,node_size=nodesize) 
    else:
        nx.draw_networkx_nodes(g,pos=pos,node_color=nodecolor,alpha=nodealpha,node_size=nodesize)
    
    labels={}
    for idx,node in enumerate(g.nodes()):
        labels[idx]=str(idx)
    
    nx.draw_networkx_labels(g,pos,labels,font_size=16)
    plt.xticks([])
    plt.yticks([])
    plt.title(title,fontsize=titlefontsize)
    if savefig and filename!=None:
        plt.savefig(filename,dpi=300)
