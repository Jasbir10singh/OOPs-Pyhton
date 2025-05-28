# from opps_proj import ChatBot

# user1 = ChatBot()

from oops import MRPChatBot

jas = MRPChatBot()

print(jas.get_name()) 

#print(jas._MRPChatBot__user_id)

jas.set_user_id(10)
print(jas.get_user_id())