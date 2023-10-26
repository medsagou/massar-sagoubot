from interaction import Massar_Sagou
from list_reader import List_Reader

if __name__ == "__main__":
    interaction_object = Massar_Sagou()
    interaction_object.main_interaction()

    list_reader = List_Reader()
    list_reader.driver = interaction_object.driver
    list_reader.main_list_reader()

    interaction_object.exit_program()