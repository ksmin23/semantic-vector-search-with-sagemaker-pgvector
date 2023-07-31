import os

import streamlit as st
import dataset

import pgvector_search


def main():
    conn_str = os.environ['POSTGRES_CONNECTION_STRING']
    dbconn = dataset.connect(conn_str)

    embeddings_model_endpoint = os.environ['EMBEDDING_ENDPOINT_NAME']
    embedding_function = pgvector_search.create_embedding_endpoint(embeddings_model_endpoint)

    st.title('AI-powered Product Catalog Search')
    search = st.text_input('Enter search words:')

    if search:
        results, took_time = pgvector_search.index_search(embedding_function, dbconn, search)

        # show number of results and time taken
        total_hits = len(results)
        st.text(f"{total_hits} results ({took_time:.2f} seconds)")

        # search results
        columns = st.columns(3)

        for i, res in enumerate(results):
            with columns[i]:
               st.markdown(f'''<div style="font-size:120%;">
                                   {i + 1}. <b>Product Item Id: {res['id']}</b>
                               </div>''', unsafe_allow_html=True)
               st.image(res['url'])
               description = res['description']
               st.markdown(f'''<div style="color:grey;font-size:95%;">
                                   {description[:90] + '...' if len(description) > 100 else description}
                               </div>''', unsafe_allow_html=True)


if __name__ == '__main__':
    main()
