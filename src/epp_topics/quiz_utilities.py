from jupyterquiz import display_quiz as display_quiz_old


def display_quiz(content):
    """Display a quiz using jupyterquiz.

    This is a thin wrapper around jupyterquiz that takes the quiz content in a simpler
    format and fills in many defaults.

    Args:
        content (dict): A dictionary with the questions and answer options.

    Example content:

    {
        "question_1": {
            "option_1": True,
            "option_2": False,
            "option_3": True
        },
        "question_2": {
            "option_1": False,
            "option_2": False,
            "option_3": True,
        },
    }
    """
    internal_content = create_quiz_content(content)
    display_quiz_old(internal_content, colors="fdsp")


def create_quiz_content(raw):
    """Translate the quiz content from our format to the jupyterquiz format."""
    out = []
    for question, answers in raw.items():
        out.append(_process_question_and_answers(question, answers))
    return out


def _process_question_and_answers(question, answers):
    internal_answers = []
    for answer, correct in answers.items():
        internal_answers.append(
            {
                "answer": answer,
                "correct": correct,
                "feedback": "Correct." if correct else "Incorrect.",
            },
        )

    return {
        "question": question,
        "type": _determine_case(answers),
        "answers": internal_answers,
    }


def _determine_case(answers):
    return "multiple_choice" if sum(answers.values()) == 1 else "many_choice"
