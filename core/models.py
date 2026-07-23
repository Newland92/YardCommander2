from dataclasses import dataclass


@dataclass
class Trailer:
    trailer: str = ""
    status: str = ""
    contents: str = ""
    tractor: str = ""
    po: str = ""
    seal: str = ""

    def needs_cleanup(self) -> bool:
        """
        Returns True if this trailer requires any changes.
        """

        if self.tractor.strip():
            return True

        if self.contents.upper() == "EMPTY":

            if self.po.strip():
                return True

            if self.seal.strip():
                return True

            if self.status.upper() == "INBOUND":
                return True

        return False

    def __str__(self):

        return (
            f"{self.trailer} | "
            f"Status={self.status} | "
            f"Contents={self.contents} | "
            f"Tractor={self.tractor} | "
            f"PO={self.po} | "
            f"Seal={self.seal}"
        )