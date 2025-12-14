from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

knowledge_base = {
    "destinations": "We offer destinations like Bali, Maldives, Dubai, Europe, and popular Indian tourist locations.",
    "pricing": "Our prices depend on destination, duration, and customization. Packages start at affordable rates.",
    "packages": "We offer honeymoon, family, group, and fully customized travel packages.",
    "process": "The booking process is simple: choose a destination, receive a quote, confirm, and we handle everything.",
    "contact": "You can reach our travel experts via phone, email, or WhatsApp."
}

topics = list(knowledge_base.keys())
topic_embeddings = model.encode(topics, convert_to_tensor=True)

def get_response(user_input, last_topic=None):
    user_embedding = model.encode(user_input, convert_to_tensor=True)
    scores = util.cos_sim(user_embedding, topic_embeddings)[0]
    best_match = scores.argmax().item()

    if scores[best_match] > 0.4:
        topic = topics[best_match]
        return knowledge_base[topic], topic

    if last_topic:
        return knowledge_base[last_topic], last_topic

    return "Could you please clarify your travel query?", None
