from collections import Counter

def deduplicate_and_rank(*result_lists):
    id_to_doc = {}
    id_counts = Counter()
    for result_list in result_lists:
        for doc in result_list:
            doc_id = doc["_id"]
            id_to_doc[doc_id] = doc
            id_counts[doc_id] += 1
    # Sort by how many lists the doc appeared in (descending)
    sorted_ids = [doc_id for doc_id, _ in id_counts.most_common()]
    return [id_to_doc[doc_id] for doc_id in sorted_ids]

