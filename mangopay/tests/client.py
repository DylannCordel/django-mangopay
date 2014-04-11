from mangopaysdk.entities.card import Card
from mangopaysdk.entities.user import User
from mangopaysdk.entities.bankaccount import BankAccount
from mangopaysdk.entities.refund import Refund
from mangopaysdk.entities.kycdocument import KycDocument
from mangopaysdk.entities.kycpage import KycPage
from mangopaysdk.entities.wallet import Wallet
from mangopaysdk.entities.cardregistration import CardRegistration
from mangopaysdk.entities.payout import PayOut
from mangopaysdk.types.money import Money


class MockMangoPayApi():

    def __init__(self, user_id=None, bank_account_id=None,
                 card_registration_id=None, card_id=None,
                 document_id=None, wallet_id=None, refund_id=None,
                 pay_out_id=None):
        self.users = MockUserApi(user_id, bank_account_id, document_id)
        self.cardRegistrations = MockCardRegistrationApi(
            card_registration_id, card_id)
        self.cards = MockCardApi(card_id)
        self.wallets = MockWalletApi(wallet_id)
        self.payOuts = MockPayOutApi(pay_out_id)
        self.payIns = MockPayInApi(refund_id)


class MockUserApi():

    def __init__(self, user_id, bank_account_id, document_id):
        self.user_id = user_id
        self.bank_account_id = bank_account_id
        self.document_id = document_id

    def Create(self, user):
        if isinstance(user, User):
            user.Id = self.user_id
            return user
        else:
            raise TypeError("User must be a User Entity")

    def CreateBankAccount(self, user_id, bank_account):
        if isinstance(bank_account, BankAccount) and isinstance(user_id, str):
            bank_account.Id = self.bank_account_id
            return bank_account
        else:
            raise TypeError("Arguements are the wrong types")

    def Update(self, user):
        if isinstance(user, User) and user.Id:
            return user
        else:
            raise TypeError("User must be a User Entity with an Id")

    def CreateUserKycDocument(self, document, user_id):
        if isinstance(document, KycDocument):
            document.Id = self.document_id
            document.Status = "CREATED"
            return document
        else:
            raise TypeError("Document must be a KycDocument entity")

    def GetUserKycDocument(self, document_id, user_id):
        document = KycDocument()
        document.Id = document_id
        document.Status = "VALIDATED"
        return document

    def UpdateUserKycDocument(self, document, user_id, document_id):
        if (isinstance(document, KycDocument)
                and document.Id == document_id
                and document.Status == "VALIDATION_ASKED"):
            return document
        else:
            raise BaseException("Arguements are of the wrong types")

    def CreateUserKycPage(self, page, user_id, document_id):
        if isinstance(page, KycPage):
            pass
        else:
            raise TypeError("Page must be a KycPage")


class MockCardApi():

    def __init__(self, card_id):
        self.card_id = card_id

    def Get(self, card_id):
        card = Card(id=card_id)
        card.Alias = "497010XXXXXX4414"
        card.ExpirationDate = "1018"
        card.Active = True
        card.Validity = "VALID"
        return card


class MockCardRegistrationApi():

    def __init__(self, card_registration_id, card_id=None):
        self.card_registration_id = card_registration_id
        self.card_id = card_id

    def Create(self, card_registration):
        if isinstance(card_registration, CardRegistration):
            card_registration.Id = self.card_registration_id
            return card_registration
        else:
            raise TypeError(
                "Card Registration must be a CardRegistration Entity")

    def Update(self, card_registration):
        if isinstance(card_registration, CardRegistration):
            card_registration.CardId = self.card_id
            return card_registration
        else:
            raise TypeError(
                "Card Registration must be a CardRegistration Entity")

    def Get(self, card_registration_id):
            card_registration = CardRegistration(card_registration_id)
            card_registration.RegistrationData = "data=RegistrationData"
            card_registration.PreregistrationData = "PreregistrationData"
            card_registration.AccessKey = "AccessKey"
            card_registration.CardRegistrationURL = "CardRegistrationURL"
            return card_registration


class MockWalletApi():

    def __init__(self, wallet_id):
        self.wallet_id = wallet_id

    def Create(self, wallet):
        if isinstance(wallet, Wallet) and not wallet.Id:
            wallet.Id = self.wallet_id
            return wallet
        else:
            raise TypeError("Wallet must be a Wallet Entity")

    def Get(self, wallet_id):
        wallet = Wallet()
        wallet.id = wallet_id
        wallet.Balance = Money(10000, currency="EUR")
        return wallet


class MockPayOutApi():

    def __init__(self, pay_out_id):
        self.pay_out_id = pay_out_id

    def Create(self, pay_out):
        if isinstance(pay_out, PayOut) and not pay_out.Id:
            pay_out.Id = self.pay_out_id
            pay_out.ExecutionDate = 12312312
            return pay_out
        else:
            raise TypeError("Wallet must be a Wallet Entity")

    def Get(self, pay_out_id):
        pay_out = PayOut()
        pay_out.Id = pay_out_id
        pay_out.ExecutionDate = 12312312
        pay_out.Status = "CREATED"
        return pay_out


class MockPayInApi():

    def __init__(self, refund_id):
        self.refund_id = refund_id

    def CreateRefund(self, pay_in_id, refund):
        if isinstance(refund, Refund) and pay_in_id:
            refund.Id = self.refund_id
            refund.ExecutionDate = 12312312
            refund.Status = "SUCCEEDED"
            return refund
        else:
            raise TypeError("Refund must be a refund entity")
