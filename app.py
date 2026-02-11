import streamlit as st
import speedtest

st.set_page_config(page_title="Internet Speed Test", page_icon="⚡")

st.title("⚡ Internet Speed Test")
st.write("Streamlit + Python se simple speed test app")

if st.button("Run Speed Test"):
    with st.spinner("Testing speed... thoda wait karo..."):
        try:
            stest = speedtest.Speedtest()
            stest.get_best_server()

            download = stest.download() / 1_000_000  # bits -> Mbps
            upload = stest.upload() / 1_000_000      # bits -> Mbps
            ping = stest.results.ping

            st.success("Test complete!")

            col1, col2, col3 = st.columns(3)
            col1.metric("Download", f"{download:.2f} Mbps")
            col2.metric("Upload", f"{upload:.2f} Mbps")
            col3.metric("Ping", f"{ping:.0f} ms")

        except Exception as e:
            st.error(f"Kuch error aaya: {e}")
else:
    st.info("Speed check karne ke liye button dabao.")
