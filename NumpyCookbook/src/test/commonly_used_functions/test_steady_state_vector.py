import unittest
from matplotlib.finance import quotes_historical_yahoo
import numpy
from datetime import date

def get_close_prices(symbol, start, end):
    quotes = quotes_historical_yahoo(symbol, start, end)
    return [q[4] for q in quotes]

def get_states(close_prices):
    return numpy.sign(numpy.diff(close_prices))

def get_stohcastic_matrix(states, signs, smoothing_constant):
    ndim = len(signs)
    stohcastic_matrix = numpy.zeros((ndim,ndim))
    
    for sign_indx_i, sign_i in enumerate(signs):
        start_indices = numpy.where(states[:-1]==sign_i)[0]
        N = len(start_indices) + smoothing_constant*ndim
        
        if N == 0:
            continue
        
        #find the values of states at the end positions
        end_values = states[start_indices+1]
        
        for sign_indx_j, sign_j in enumerate(signs):
            # number of occurrences of this transition 
            occurrences = len(end_values[end_values == sign_j])
            stohcastic_matrix[sign_indx_i][sign_indx_j] = (occurrences + smoothing_constant)/float(N)
            
    return stohcastic_matrix

def get_meta_state_index(name):
    states = numpy.array([['down_down','down_same','down_up'],
                          ['same_down','same_same','same_up'],
                          ['up_down','up_same','up_up']])
    indices = numpy.where(states[:-1] == name)
    if len(indices) > 0:
        return indices[0][0],indices[1][0]
    return None
    
class SteadyStateVectorTest(unittest.TestCase):


    def test(self):
        today = date.today()
        start = (today.year - 1, today.month, today.day)
        close_prices = get_close_prices('AAPL', start, today)
        states = get_states(close_prices)
        signs = [-1,0,1]
        stohcastic_matrix = get_stohcastic_matrix(states,signs,1)
        
        eig_value, eig_vector = numpy.linalg.eig(stohcastic_matrix)
        steady_state_eigen_value_indx = numpy.where(numpy.abs(eig_value - 1) < 0.1)
        steady_state_eigen_vector = eig_vector[:,steady_state_eigen_value_indx]
        numpy.testing.assert_array_almost_equal(steady_state_eigen_vector.flatten(), numpy.dot(stohcastic_matrix,steady_state_eigen_vector.flatten()))
        steady_state_eigen_vector = numpy.ravel(steady_state_eigen_vector)
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()