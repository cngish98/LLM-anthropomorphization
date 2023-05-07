"""Metrics for baseline model."""

from sklearn import metrics


class Metrics:
    def __init__(self, true, predicted):
        """
        :param true: list of true labels
        :param predicted: list of predicted labels
        """
        self.true = true
        self.predicted = predicted

    def get_metrics(self):
        """Compute accuracy, F1 score, and confusion matrix."""
        accuracy = metrics.accuracy_score(self.true, self.predicted)
        print(accuracy)
        f1_score = metrics.f1_score(self.true, self.predicted)
        print(f1_score)
        conf_matrix = metrics.confusion_matrix(self.true, self.predicted)
        print(conf_matrix)

        return accuracy, f1_score, conf_matrix
