# =============================================================================
# Funções para Modelagem de Tópicos
# =============================================================================
import numpy as np

# Coletar tópicos e seus pesos
def get_topics_terms_weights(weights, feature_names):
    feature_names = np.array(feature_names)
    sorted_indices = np.array([list(row[::-1]) for row in np.argsort(np.abs(weights))])
    sorted_weights = np.array([list(wt[index]) for wt, index in zip(weights, sorted_indices)])
    sorted_terms = np.array([list(feature_names[row]) for row in sorted_indices])
    
    topics = [np.vstack((terms.T, term_weights.T)).T for terms, term_weights in zip(sorted_terms, sorted_weights)]
    
    return topics

# Imprimir os componentes de cada tópico
def print_topics_udf(topics, total_topics=1, weight_threshold=0.0001, display_weights=False, num_terms=None):
    
    for index in range(total_topics):
        topic = topics[index]
        topic = [(term, float(wt))
                 for term, wt in topic]
        topic = [(word, round(wt,2)) 
                 for word, wt in topic 
                 if abs(wt) >= weight_threshold]
                     
        if display_weights:
            print('Tópico #'+str(index)+' (com pesos)')
            print(topic[:num_terms]) if num_terms else topic
        else:
            print('Tópico #'+str(index+1))
            tw = [term for term, wt in topic]
            print(tw[:num_terms]) if num_terms else tw

