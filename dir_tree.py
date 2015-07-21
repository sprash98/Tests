



import os

class Node() :

    # Tree class

    """ Class that denotes the tree. Contains the root of the tree and a
        dictionary that maps the tree. Includes methods to create the
        tree, obtain the information of a node's children and to
        return the details of a node
    """

    tree = {}

    # Root of tree
    root = ''

    # Function to create the tree

    def __init__(self,node):

        """ This function creates the tree. It takes in a directory and maps
         out all files and subdirectories of the directory. The structure
         returned is a dictionary, where the keys are the directories
         and the value is an array where the first element is a list of
         all subdirectories and the second element is a
         dictionary where the keys are the files and the values are
         the filesizes, in bytes """

        # If node is not of type string, abort
        if type(node) != str :
            print("Please enter root directory as a string. Aborting...")
            return None

        # If node is an empty string, abort
        if node == '' :
            print("Please supply a valid string for root directory")
            return None

        # If node is not a valid directory, abort
        if not os.path.isdir(node) :
            print("Supplied value %s is not a valid directory" %(node))
            return None

        # Walk the contents of the directory and create the tree
        contents = os.walk(node)

        self.root = node
        for val in contents :
            curr_dir = val[0]
            sub_dir = val[1]
            files = {}

            for file in val[2] :
                size = list(os.stat(curr_dir+ "\\"+ file))[6]
                files[file] = int(size)

            self.tree[curr_dir] = [sub_dir,files]


    # Function to get the children of a node
    def getChildren(self,node) :

        """
        :param node: Directory whose children is desired
        :return: A list of two elements, where the first element
                is a list of subdirectories, while the second
                element is a dictionary of files and filesizes

        The function takes in a node and returns a list of subdirectories and
        files of that directory. Returns an empty list if supplied directory
        is invalid
        """

        # Abort if supplied directory is not of type string
        if type(node) != str :
            print("Please enter a valid string for the node. Aborting...")
            return []

        # Abort if empty directory is supplied
        if node == '' :
            print("Please enter a non-empty string for root directory. Aborting...")
            return []

        # If the directory supplied is not a key in the tree, abort.
        if node not in self.tree.keys() :
            print('Supplied root %s is not a valid directory or subdirectory of %s' %(node,self.root))
            return []

        return self.tree[node]


    def getFileInfo(self,node):

        """
        :param node: File whose information is required
        :return: A dictionary where the key is the directory where file is found
                and the value is the size of the file in the directory. This
                function detects multiple files of the same name in different
                subdirectories
        """

        file_info = {}
        for dity in self.tree :

            files_in_dir = self.tree[dity][1]
            if node in files_in_dir :
                file_info[dity] = files_in_dir[node]

        return file_info


    def getDetail(self,node) :

        """
        :param node: Directory or file whose information is required
        :return: A dictionary. For a directory, the keys are
                 number of subdirectories and files. For a file,
                 the keys are directories where the file is found
                 and the sizes of the file in those directories
        """

        info = {}

        # Abort if supplied value is not a string
        if type(node) != str :
            print("Please enter a valid string for the root. Aborting...")
            return info

        # Abort if supplied value is an empty string
        if node == '' :
            print("Please enter a non-empty string for root directory. Aborting...")
            return info

        # If supplied value is a file
        if node not in self.tree.keys() :
            file_info = self.getFileInfo(node)
            if list(file_info.keys()) == [] :
                print("Specified object %s is neither a file nor a directory in the tree" \
                      %(node) )
                return info

            return file_info

        # If supplied value is a directory, obtain the number of subdirectories
        # and files in that directory. The code DOES NOT count the number of
        # files in the subdirectories
        else :
            dir_content = {}
            contents = self.tree[node]
            dir_content['Subdir'] = len(contents[0])
            dir_content['Files'] = len(contents[1])
            return dir_content


node = input("Please enter directory you want to map: ")
tree = Node(node)
if tree.root == '' :
    print("Unable to create tree. Exiting...")
    exit()

root = input("Please enter a directory whose children you need : ")
children = tree.getChildren(root)

if children:
    if children[0] :
        print("Subdirectories in %s are : " % root, end = ' ')
        print(*children[0], sep = ',')
    else :
        print("%s has no subdirectories" %(root))

    if children[1] :
        print ("Files in directory %s are:  " % root, end = ' ')
        print(*children[1], sep = ', ')
    else :
        print("%s has no files" %(root))


req = input("Please enter a file or directory whose information you need. "
            "Do not specify the path for file. Specify whole path for directory: ")
details = tree.getDetail(req)

if details :
    if 'Subdir' in details :
        print('The directory %s has %d subdirectories and %d files' %(req,details['Subdir'],details['Files']))
    else:
        print("The file %s was found in the following locations on the tree" %(req))
        for loc in details :
            print("Directory: %s Size: %s KB" %(loc,details[loc]/100))





















