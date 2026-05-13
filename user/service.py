# from .models import User
# def create_user(validated_data):
#     user = User.objects.create_user(**validated_data)
#     user.save()
#     return user
#
#
#
#
#
#
#  #
#  # <div className={Style.grid}>
#  #                {users.map((user)=>(
#  #                    <div key={user._id} className={Style.cards}>
#  #                        <div className={Style.avatar} style={{backgroundColor: user.status === "online" ? "#4ade80" : "#94a3b8"}}></div>
#  #                    </div>
#  #                ))}
#  #            </div>
#
#
# // import
#
# {useEffect, useState}
# from
#
# "react"
# // import Style
# from
#
# "./dashboard.module.css"
# // import
#
# {useNavigate}
# from
#
# "react-router-dom"
# // import axios
# from
#
# "axios"
#
# // export
# default
# function
# Dashboard()
# {
# // const
# navigate = useNavigate() \
#            // const[users, setUsers] = useState([]);
#http://localhost:3000/api/v1/auth/login
# // const
# token = localStorage.getItem("token")
#         // const
# currentUser = JSON.parse(localStorage.getItem("user") | | "{}")
#
#               // useEffect(() = > {
#                                   // const
# fetchUsers = async () = > {
#                           //
# try{
# // const res = await axios.get("http://localhost:3000/api/v1/auth/users", {
# // headers: {
#             // Authorization: `Bearer ${token}
# `
# //}
# //})
# // setUsers(res.data.users)
#
#    // console.log(res.data)
#    //}catch(error)
# {
# // console.log(error)
# //}
#
# //}
# // fetchUsers();
#
# //}, []);
#
# // const
# logout = () = > {
#                 // localStorage.clear()
#                 // navigate("/login")
#                 //}
#
# // return (
#     // < div className={Style.Container} >
#     // < div className={Style.header} >
#     // < h2 > CALLER < / h2 >
#
#     // < div >
#     // < span > {currentUser?.userName} < / span >
#     // < button className={Style.logoutBtn} onClick={logout} > Logout < / button >
#     // < / div >
#     // < / div >
#
#     // < / div >
#     //)
# //}