"""Takes a letter and rewturns ascii art for that letter"""


letter_art_text = {'a':
"""
            
    ####    
   ##  ##   
  ##    ##  
  ########  
  ##    ##  
            
"""
,'b':
"""
            
  #######   
  ##    ##  
  #######   
  ##    ##  
  #######   
            
"""
,'c':
"""
            
   #######  
  ##        
  ##        
  ##        
   #######  
            
"""
,'d':
"""
            
  #######   
  ##    ##  
  ##    ##  
  ##    ##  
  #######   
            
"""
,'e':
"""
            
  ########  
  ##        
  #####     
  ##        
  ########  
            
"""
,'f':
"""
            
  ########  
  ##        
  ######    
  ##        
  ##        
            
"""
,'g':
"""
            
  ########  
  ##        
  ##  ####  
  ##    ##  
  ########  
            
"""
,'h':
"""
            
  ##    ##  
  ##    ##  
  ########  
  ##    ##  
  ##    ##  
            
"""
,'i':
"""
            
   ######   
     ##     
     ##     
     ##     
   ######   
            
"""
,'j':
"""
            
   #######  
      ##    
      ##    
  #   ##    
   ####     
            
"""
,'k':
"""
            
  ##  ###   
  ## ##     
  ####      
  ## ##     
  ##  ###   
            
"""
,'z':
"""
            
            
            
            
            
            
            
"""
}

letter_art_color = {'a': ['grey','white'],'b':['cyan','white'],'c':['blue','white'],'d':['magenta','white'],'e': ['white','magenta'],'f': ['white','green'],
                    'g': ['white','red'],'h': ['white','blue'],'i':['magenta','blue'],'j':['green','yellow'],'k':['magenta','green'],'z':['white','white']}

def get_letterart_txt(letter):
    return letter_art_text[letter]

def get_letterart_col(letter):
    return letter_art_color[letter]