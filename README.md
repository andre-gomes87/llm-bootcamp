# LLM Bootcamp

My journey from LLM enthusiast to practitioner, documented through weekly projects and hands-on exploration.

## 📋 Overview

This is a personal project-based learning path I'm building to deeply understand Large Language Models. Rather than just reading papers or following courses, I'm learning by doing—each week brings a new project that builds on previous knowledge and pushes me further into the LLM ecosystem.

### Learning Path
- **Week 1-4:** Foundations—understanding how LLMs work
- **Week 5-8:** Going deeper—advanced techniques and customization
- **Week 9-12:** Getting practical—building real applications
- **Week 13+:** Specialized exploration and integrating everything

## 🎯 What I'm Working Towards

- Understanding the architecture and mechanics of LLMs
- Getting proficient at prompt engineering
- Building functional LLM applications
- Learning to fine-tune and adapt models
- Understanding production considerations
- Working with RAG systems and retrieval
- Exploring the boundaries and possibilities

## 📚 Project Structure

```
llm-bootcamp/
├── week-01/          # Project 1
├── week-02/          # Project 2
├── week-03/          # Project 3
├── ...
├── week-12/          # Project 12
├── capstone/         # Final project
└── README.md
```

Each week contains:
- `project.md` - Project description and requirements
- `assessment.md` - Assessment questions to validate learning
- `solution/` - Reference implementation
- `notebooks/` - Jupyter notebooks for exploration
- `data/` - Sample datasets (if applicable)

### Assessment Files

Every week includes an assessment file designed to test understanding through hands-on experimentation. The assessment follows these principles:

- **Base your answers on your own experiments**
- **Do not copy from docs or Google**
- **NO AI GENERATED ANSWERS**

The goal is to ensure genuine learning through direct interaction with the concepts, not just regurgitating documentation.

## 🛠️ Prerequisites

Before starting, ensure you have:
- Python 3.8+ installed
- Basic Python programming knowledge
- Familiarity with Git and command-line tools
- API keys for LLM services (OpenAI, HuggingFace, etc.)
- Optional but recommended: GPU access for training tasks

## 🚀 Getting Started

1. **Set up the environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure API keys:**
   Create a `.env` file with API keys as needed:
   ```
   OPENAI_API_KEY=your_key_here
   HUGGINGFACE_API_KEY=your_key_here
   ```

3. **Start exploring:**
   Each week folder contains a project, notebooks, and notes from that phase of learning.

## 📖 Weekly Projects

| Week | Topic | Focus |
|------|-------|-------|
| 1 | LLM Fundamentals | Understanding transformers and language models |
| 2 | Prompt Engineering | Techniques for effective prompting |
| 3 | API Integration | Building with OpenAI, HuggingFace APIs |
| 4 | Context & Memory | Implementing conversation memory |
| 5 | RAG Systems | Retrieval-Augmented Generation |
| 6 | Vector Databases | Working with embeddings and vector stores |
| 7 | Fine-tuning Basics | Adapting models to specific tasks |
| 8 | Evaluation Metrics | Measuring LLM performance |
| 9 | Web Application | Building full-stack LLM applications |
| 10 | Deployment | Containerizing and deploying models |
| 11 | Optimization | Quantization, caching, and inference speed |
| 12 | Advanced Techniques | Multi-agent systems, tool use |
| 13+ | Capstone Project | Apply everything in a real-world scenario |

## 💡 Key Topics Covered

- **Transformers Architecture** - How LLMs work
- **Tokenization & Embeddings** - Input representation
- **Prompt Engineering** - Effective communication with models
- **API Usage** - Integrating with commercial LLM services
- **Retrieval-Augmented Generation (RAG)** - Grounding models with external data
- **Fine-tuning & Adaptation** - Customizing models
- **Vector Databases** - Semantic search and similarity
- **Evaluation Frameworks** - Assessing model quality
- **Production Deployment** - Scaling LLM applications
- **Optimization Techniques** - Performance and cost efficiency
- **Safety & Ethics** - Responsible AI development
- **Multi-agent Systems** - Complex LLM orchestration

## 🧑‍💻 How This Project is Organized

- Each week is a self-contained project
- Projects build on previous weeks but are designed to stand alone
- Mix of notebooks for exploration and Python scripts for implementation
- Notes and reflections included alongside the code
- Reference materials and resources collected as I go

## 📦 Dependencies

Key libraries used throughout the bootcamp:
- `openai` - OpenAI API client
- `langchain` - LLM application framework
- `transformers` - HuggingFace transformer models
- `torch` - PyTorch deep learning framework
- `pinecone-client` - Vector database
- `jupyter` - Interactive notebooks
- `python-dotenv` - Environment variable management

## 🤝 Contributing

This is a personal project, so I'm not actively seeking contributions. That said, if you're following a similar path and want to share insights or point out issues, feel free to open an issue or reach out.

## 🎓 Learning Approach

I'm learning by building. Rather than trying to consume everything at once, each week has a focused project that forces me to engage with new concepts practically. The goal is depth through application, not breadth through reading.

## 📞 Context

These notes and projects are primarily for my own learning process. If you're exploring LLMs yourself, you might find some of the approaches or resources useful. Otherwise, think of this as documentation of one developer's learning journey.

If you have suggestions or comments feel free to reach out, I would love to hear about your experience !!!

---

*Started: April 2026*
