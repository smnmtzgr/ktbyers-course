def list_to_dict(a_list):
    a_dict = {}
    for i,element in enumerate(a_list):
        a_dict[i] = element

    return a_dict

# Create a simple test list
test_list = range(100, 110)
test_list.append('whatever')

# Call the function
test_dict = list_to_dict(test_list)

# Display the results
print
print "List: %s" % str(test_list)
print "Dict: %s" % str(test_dict)
print
