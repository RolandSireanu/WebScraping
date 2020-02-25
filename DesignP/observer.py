from abc import ABCMeta, abstractmethod, ABC
from typing import List 
class Observer(ABC):

    @abstractmethod
    def update(self , arg_subject) -> None:
        pass

class ObserverA(Observer):

    def update(self , arg_subject) -> None:
        #Receives updates from Subject
        print("ObserverA update()")


class ObserverB(Observer):

    def update(self , arg_subject) -> None:
        print("ObserverB update()")



class Subject(ABC):

    def _init__(self):
        pass

    @abstractmethod
    def attach(self , observer:Observer) -> None:
        pass

    @abstractmethod
    def detach(self , observer:Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class ConcreteSubject(Subject):

    def __init__(self):
        self.observers:List[Observer] = []

    def attach(self , observer:Observer) -> None:
        self.observers.append(observer)
        print("ConcreteSubject attach ")

    def detach(self , observer:Observer) -> None:
        print("ConcreteSubject detach ")

    def notify(self) -> None:
        for o in self.observers:
            o.update(self)
        print("ConcreteSubject notify ")

    def smartMethod(self) -> None:
        for i in range(10):
            pass
        self.notify()




obs = ObserverA()
obs2 = ObserverA()
obs3 = ObserverB()
subject = ConcreteSubject()
subject.attach(obs)
subject.attach(obs2)
subject.attach(obs3)
subject.smartMethod()




