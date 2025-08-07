import numpy as np
class Create_a_array:
    def __init__(self):
        pass
    def create_1D_array(self):
        try:
           self.element = input("Enter the elements of the array, Sepreted by space: ")
           self.elements_list = list(map(int, self.element.split()))
           self.array = np.array(self.elements_list)
           print("array create successfully")
           print("1D array: ",self.array)
        except ValueError:
           print("Input Error: Please enter valid integers.")
        except Exception as e:
           print(f"Unexpected error: {e}")

    def create_2D_array(self):
        try:
          self.row = int(input("enter the number of row: "))
          self.coloumns = int(input("Enter the number of coloumns: "))
          self.total_elements = self.row * self.coloumns
          self.element = input(f"Enter {self.total_elements} elements of the array, sepreted by space: ")
          self.elements_list = list(map(int,self.element.split()))
          self.origneal_array = np.array(self.elements_list).reshape(self.row,self.coloumns)
          print("2D array created successfully")
          print("2D array: "
              ,self.origneal_array)
        except ValueError:
            print("Input Error: Please enter valid integers.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def addition_array(self):
        try: 
            self.element = input(f"enter the same size array ({self.total_elements} elements sepreted by space): ")
            self.elements_list = list(map(int,self.element.split()))
            self.second_array = np.array([self.elements_list]).reshape(self.row,self.coloumns)
            self.addition = self.origneal_array + self.second_array
            print("result fo addition: ")
            print(self.addition)
        except ValueError:
            print("Input Error: Please enter valid integers.")
        except Exception as e:
            print(f"Unexpected error: {e}")
        

    def subtraction_array(self):
        try: 
           self.element = input(f"Enter the same size ({self.total_elements} elements sepreded bi space): ")
           self.elements_list = list(map(int,self.element.split()))
           self.second_array = np.array([self.elements_list]).reshape(self.row, self.coloumns)
           self.subtraction = self.origneal_array - self.second_array
           print("result of subtraction: ")
           print(self.subtraction)
        except ValueError:
            print("Input Error: Please enter valid integers.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def multiplication_array(self):
        try: 
           self.element = input(f"Enter the same size of array ({self.total_elements} Elements sepreted by space): ")
           self. elements_list = list(map(int,self.element.split()))
           self.second_array = np.array([self.elements_list]).reshape(self.row,self.coloumns)
           self.multiplication = self.origneal_array * self.second_array
           print("result of multiplication: ")
           print(self.multiplication)
        except ValueError:
            print("Input Error: Please enter valid integers.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def divided_array(self):
        try: 
           self.element = input(f"Enter the same size of array ({self.total_elements} Elements sepreted by space): ")
           self. elements_list = list(map(float,self.element.split()))
           self.second_array = np.array([self.elements_list]).reshape(self.row,self.coloumns)
           self.division = self.origneal_array / self.second_array
           print("result of division: ")
           print(self.division)
        except ValueError:
            print("Input Error: Please enter valid integers.")
        except Exception as e:
            print(f"Unexpected error: {e}")


    def combine_array_verticaly(self):
        try: 
          self.element = input(f"enter the anather array to combine ({self.total_elements} seprated by space): ")
          self.elements_list = list(map(int,self.element.split()))
          self.second_array  = np.array([self.elements_list]).reshape(self.row,self.coloumns)
          self.combine = np.concatenate((self.origneal_array,self.second_array),axis=0)
          print("Combine array (Verticle stac): ")
          print(self.combine)
        except ValueError:
            print("Input Error: Please enter valid integers.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    
    def combine_array_hirizentaly(self):
        try: 
           self.element = input(f"enter the anather array to combine ({self.total_elements} seprated by space): ")
           self.elements_list = list(map(int,self.element.split()))
           self.second_array  = np.array([self.elements_list]).reshape(self.row,self.coloumns)
           self.combine = np.concatenate((self.origneal_array,self.second_array),axis=1)
           print("Combine array (Horizental stac): ")
           print(self.combine)
        except ValueError:
            print("Input Error: Please enter valid integers.")
        except Exception as e:
            print(f"Unexpected error: {e}")
        
    def sort_the_array(self):
        try: 
           self.sorted_array = np.sort(self.origneal_array)
           print("sorted array: ")
           print(self.sorted_array)
        except ValueError:
            print("Input Error: Please enter valid integers.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def sum_of_the_array(self):
        try:
           self.sum = np.sum(self.origneal_array)
           print("sum of all elements: ")
           print(self.sum)
        except ValueError:
            print("Input Error: Please enter valid integers.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    
    def create_3D_array(self):
        self.row = int(input("Enter the element of the row: "))
        self.coloumns = int(input("Enter the number of coloumns: "))
        self.total_elements = self.row * self.coloumns * 2
        self.element = input(f"Enter {self.total_elements } elements of the array, sepreted by space: ")
        self.elements_list= list(map(int,self.element.split()))

      # Validate if the number of elements matches the required total elements
        if len(self.elements_list) != self.total_elements:
            print(f"Error: You need to enter exactly {self.total_elements} elements.")
            return
       
        self.array = np.array([self.elements_list]).reshape(self.row,self.coloumns,2)
        print("3D array created successfully")
        print("3D array: ",self.array)












ca = Create_a_array()

print("welcome to the numpy anylizer!")
print("=" * 40)
while True:
    print("select an option: ")
    print("1. create numpy array")
    print("2. parform mathemeticle oprection")
    print("3. combine or split array")
    print("4. search, sort, or filtter array")
    print("5. compute aggrigate and statastic")
    print("6. exit")

    option = int(input("enter your choice: "))

    match option:
        case 1:
            while True:
                print("select the type of array to create: ")
                print("1. 1D array")
                print("2. 2D array")
                print("3. 3D array")
                print("4. Go to main menu")

                option = int(input("enter your option: "))

                match option:
                    case 1:
                        ca.create_1D_array()
                    case 2:
                        ca.create_2D_array()
                    case 3:
                        ca.create_3D_array()
                    case 4:
                        pass
                        break
        case 2:
            while True:
                print("Perform mathemetical oprection: ")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. division")
                print("5. Go to main menu")

                option = int(input("Enter your option: "))

                match option:
                    case 1:
                        ca.addition_array()
                    case 2:
                        ca.subtraction_array()
                    case 3:
                        ca.multiplication_array()
                    case 4:
                        ca.divided_array()
                    case 5:
                        pass
                        break

        case 3:
            while True:
                print("combine and split array")
                print("1. combine the array")
                print("2. split the array")
                print("3. Go to the main menu")

                option = int(input("Enter your option: "))

                match option:
                    case 1:
                        while True:

                            print("Combine the array")
                            print("1. vertical Concatinate")
                            print("2. horizentaly Concatinate")
                            print("3. Go to main menu")

                            option = int(input("Enter your option: "))

                            match option:
                                case 1:
                                    ca.combine_array_verticaly()
                                case 2:
                                    ca.combine_array_hirizentaly()
                                case 3:
                                    pass
                                    break

                    case 2:
                        print("split the array: ")

                    case 3:
                        pass
                        break


        case 4:
            while True:
                print("search, sort, and filtter array")
                print("1. search the array")
                print("2. sort the array")
                print("3. filter the array")
                print("4. Go to the main menu")

                option = int(input("enter your option: "))

                match option:
                    case 1:
                        pass
                    case 2:
                        print("sort the array: ")
                        ca.sort_the_array()
                    case 3:
                        pass
                    case 4:
                        pass
                        break
        case 5:
            while True:

                print("compute aggrigate and statastic")
                print("1. sum")
                print("2. mean")
                print("3. midian")
                print("4. standerd deveaction ")
                print("5. veriance")
                print("6. Go to main menu")

                option = int(input("Enter your choice: "))

                match option:
                    case 1:
                        ca.sum_of_the_array()
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        pass
                    case 6:
                        pass
                        break


        case 6:
            print("Thank you for using numpy anylizer! Goodby")
            break






