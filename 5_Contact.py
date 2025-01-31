import streamlit as st
st.header(":red[Contact Me: ]")
col1, col2, col3=st.columns(3)
col1=st.write("Feel free to reach out to me through the following channels: ")

col2=st.write("📧 Email : [velagasseth@gmail.com](mailto:velagasseth@gmail.com)")
col2=st.write("📞Tell : [+254759812041]()")
col2=st.write("💻 GitHub : [https://github.com/Velagasseth](https://github.com/Velagasseth)")
col2=st.write("🔗 Linkedin : [www.linkedin.com/in/velagasseth-tech](www.linkedin.com/in/velagasseth-tech)")
st.markdown("Or send me a message directly below :")
contact_form="""
<form action="https://formsubmit.co/18b9e918afc34554631e10b79ad61f98" method="POST">
<input type="hidden"
name="_captcha" value="false">
<input type="text"  name="name" placeholder="Your Name" required><br><br>
<input type="email" name="email" placeholder="Your Email" required><br><br>
<textarea  name="message" placeholder="Your Message" rows="4" required></textarea><br>
<button type="submit">Send</button>
</form>
  """
st.markdown(contact_form, unsafe_allow_html=True)