import time
from typing import List, Tuple

import numpy as np

from sagemaker.predictor import Predictor
from sagemaker.serializers import JSONSerializer
from sagemaker.deserializers import JSONDeserializer


def create_embedding_endpoint(endpoint_name: str):
    predictor = Predictor(endpoint_name=endpoint_name,
                          serializer=JSONSerializer(),
                          deserializer=JSONDeserializer())
    return predictor


def get_embeddings(predictor, text: str) -> List:
    input_data = {"inputs": text}
    model_output = predictor.predict(data=input_data)
    ndarr = np.array(model_output)
    ret = ndarr[:, 0, :].reshape(ndarr.shape[-1])
    return ret.tolist()


def index_search(embedding_function, dbconn, keywords: str) -> Tuple:
    st = time.time()

    embedding_vector = get_embeddings(embedding_function, keywords)
    query = f"""SELECT id, url, description
FROM products
ORDER BY description_embeddings <-> '{embedding_vector}'
LIMIT 3;"""

    resultset = dbconn.query(query)
    ret = list(resultset)

    et = time.time() - st
    return ret, et

