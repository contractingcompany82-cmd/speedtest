import streamlit as st
import speedtest

st.set_page_config(page_title="Internet Speed Test", page_icon="⚡")

st.title("⚡ Internet Speed Test")
st.write("Streamlit + Python se updated speed test (403 fix)")

if st.button("Run Speed Test"):
    with st.spinner("Testing speed... please wait..."):
        try:
            # FIX: secure=True to avoid 403 Forbidden
            stest = speedtest.Speedtest(secure=True)
            stest.get_best_server()

            download = stest.download() / 1_000_000  # bits → Mbps
            upload = stest.upload() / 1_000_000      # bits → Mbps
            ping = stest.results.ping

            st.success("Speed Test Completed!")

            col1, col2, col3 = st.columns(3)
            col1.metric("Download", f"{download:.2f} Mbps")
            col2.metric("Upload", f"{upload:.2f} Mbps")
            col3.metric("Ping", f"{ping:.0f} ms")

        except Exception as e:
            st.error("Kuch error aaya:")
            st.code(str(e))

else:
    st.info("Speed test start karne ke liye button dabao.")
